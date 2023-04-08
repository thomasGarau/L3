package exo3;

public class PreSave extends Event {

	public PreSave() {
		super("preSave");
	}

	public void traiter(EventInterceptor ei, Object entity){
		ei.preSave(entity);
	}
		
	

}
